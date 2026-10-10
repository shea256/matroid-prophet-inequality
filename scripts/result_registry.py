#!/usr/bin/env python3
"""Validate explicitly selected, versioned results against exact certificates."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_FIELDS = ('simplified_guarantee', 'certified_coefficient_lower_bound',
                      'seed_bits', 'parameters', 'base')


def local_path(root, name):
    if not isinstance(name, str) or Path(name).is_absolute():
        raise ValueError('Expected a repository-relative path: '+str(name))
    path = (root/name).resolve()
    if root.resolve() not in path.parents or not path.is_file():
        raise ValueError('Missing or out-of-repository file: '+name)
    return path


def field(data, dotted):
    for key in dotted.split('.'):
        data = data[key]
    return data


def guarantee_value(result):
    exponent = result['exponent']
    multiplier = Fraction(result.get('multiplier', 1))
    if not isinstance(exponent, int) or exponent < 0 or multiplier <= 0:
        raise ValueError('Expected a positive multiplier and nonnegative integer exponent')
    value = multiplier / 2**exponent
    if value > 1:
        raise ValueError('Simplified guarantee exceeds one')
    return value


def guarantee_text(result):
    guarantee_value(result)
    multiplier = Fraction(result.get('multiplier', 1))
    power = '2^-'+str(result['exponent'])
    if multiplier == 1:
        return power
    prefix = str(multiplier) if multiplier.denominator == 1 else '('+str(multiplier)+')'
    return prefix+'*'+power


def load(root=ROOT):
    registry = json.loads(local_path(root, 'results/registry.json').read_text())
    if registry.get('schema') != 1:
        raise ValueError('Unsupported registry schema')
    entries = registry['results']
    ids = [r['id'] for r in entries]
    if len(set(ids)) != len(ids) or any(not re.fullmatch(r'[a-z0-9][a-z0-9-]*', i) for i in ids):
        raise ValueError('Result IDs must be unique lowercase identifiers')
    if registry['current'] not in ids:
        raise ValueError('Current result is not registered')
    for result in entries:
        if result['status'] not in ('historical', 'proposed', 'candidate'):
            raise ValueError('Unknown result status: '+result['id'])
        local_path(root, result['record'])
        if result['status'] == 'candidate':
            continue
        cert = json.loads(local_path(root, result['certificate']).read_text())
        coefficient = Fraction(field(cert, result['coefficient_field']))
        if coefficient != Fraction(result['coefficient']):
            raise ValueError('Registry/certificate coefficient mismatch: '+result['id'])
        if field(cert, result['guarantee_field']) != guarantee_text(result):
            raise ValueError('Registry/certificate guarantee mismatch: '+result['id'])
        if not 0 < coefficient <= 1 or coefficient <= guarantee_value(result):
            raise ValueError('Coefficient does not exceed its stated simplified guarantee')
        for check in result.get('checks', []):
            local_path(root, check['script'])
            local_path(root, check['reference'])
        if 'archive' in result:
            manifest = json.loads(local_path(root, result['archive']+'/manifest.json').read_text())
            if manifest['result_id'] != result['id']:
                raise ValueError('Archive belongs to a different result')
    current = entries[ids.index(registry['current'])]
    if current['status'] != 'proposed':
        raise ValueError('Current result must have a written proposed proof; candidates and historical records cannot be selected')
    cert = json.loads(local_path(root, current['certificate']).read_text())
    for key in CERTIFICATE_FIELDS:
        if key not in cert:
            raise ValueError('Selected certificate is missing '+key)
    for check in registry['shared_checks']+registry['extended_checks']:
        local_path(root, check['script'])
        local_path(root, check['reference'])
    return registry, current, cert


def checks(registry, full=False):
    requested = list(registry['shared_checks'])
    for result in registry['results']:
        if result['status'] != 'candidate':
            requested.extend(result.get('checks', []))
    if full:
        requested.extend(registry['extended_checks'])
    unique = {}
    for check in requested:
        previous = unique.setdefault(check['script'], check)
        if previous != check:
            raise ValueError('Conflicting references for '+check['script'])
    return list(unique.values())


def archive_hashes(root=ROOT):
    """Validate every historical manifest and return immutable snapshot paths."""
    paths = set()
    manifests = sorted((root/'archive').glob('**/manifest.json'))
    for manifest_path in manifests:
        manifest = json.loads(manifest_path.read_text())
        seen = set()
        for item in manifest['files']:
            name = (manifest_path.parent.relative_to(root)/item['path']).as_posix()
            path = local_path(root, name)
            if manifest_path.parent.resolve() not in path.parents or name in seen:
                raise ValueError('Invalid archive member: '+name)
            seen.add(name)
            data = path.read_bytes()
            if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
                raise ValueError('Archived artifact changed: '+name)
            paths.add(path)
    return paths
