from pathlib import Path
import json

event_files = ['cache_retired.json', 'cache_spec.json', 'prediction_retired.json',
               'prediction_spec.json', 'rvv_retired.json', 'rvv_spec.json',
               'tlb_retired.json', 'tlb_spec.json', 'topdown.json',
               'general.json', 'retired.json', 'spec.json']

metric_files = ['cache_retired_metrics.json', 'cache_spec_metrics.json',
                'prediction_metrics.json', 'rvv_retired_metrics.json', 'rvv_spec_metrics.json',
                'tlb_retired_metrics.json', 'tlb_spec_metrics.json', 'topdown_metrics.json',
                'general_metrics.json']

file_to_group = {'cache_retired.json': 'CACHE_RETIRED',
                 'cache_spec.json': 'CACHE_SPEC',
                 'prediction_retired.json': 'PRD_RETIRED',
                 'prediction_spec.json': 'PRD_SPEC',
                 'rvv_retired.json': 'RVV_RETIRED',
                 'rvv_spec.json': 'RVV_SPEC',
                 'tlb_retired.json': 'TLB_RETIRED',
                 'tlb_spec.json': 'TLB_SPEC',
                 'topdown.json': 'TOPDOWN',
                 'general.json': 'GEN',
                 'retired.json': 'RETIRED',
                 'spec.json': 'SPEC',
                 'cache_retired_metrics.json': 'CACHE_RETIRED',
                 'cache_spec_metrics.json': 'CACHE_SPEC',
                 'prediction_metrics.json': 'PRD_RETIRED',
                 'rvv_retired_metrics.json': 'RVV_RETIRED',
                 'rvv_spec_metrics.json': 'RVV_SPEC',
                 'tlb_retired_metrics.json': 'TLB_RETIRED',
                 'tlb_spec_metrics.json': 'TLB_SPEC',
                 'topdown_metrics.json': 'TOPDOWN',
                 'general_metrics.json': 'GEN'
                 }


def generate_event_adoc(data, out_file, group_name):
    out_file.write('.' + group_name + ' group events\n')
    out_file.write('[%unbreakable]\n')
    out_file.write('[width="100%",cols="30%,70%",options="header",]\n')
    out_file.write('|===\n')
    out_file.write('|Name |Description\n')
    for event in data:
        name = event['EventName']
        desc = event['PublicDescription']
        out_file.write('|' + name + ' |' + desc + '\n')
    out_file.write('|===\n\n')
    out_file.write('[%unbreakable]\n')
    return


def generate_metric_adoc(data, out_file, group_name):
    out_file.write('.' + group_name + ' group metrics\n')
    out_file.write('[%unbreakable]\n')
    out_file.write('[width="100%",cols="25%,40%,35%",options="header",]\n')
    out_file.write('|===\n')
    out_file.write('|Name |Description |Formula\n')
    for metric in data:
        name = metric['MetricName']
        desc = metric['PublicDescription'] if 'PublicDescription' in metric else metric['BriefDescription']
        formula = metric['MetricExpr']
        out_file.write('|' + name + ' |' + desc + ' |' + formula + '\n')
    out_file.write('|===\n\n')
    out_file.write('[%unbreakable]\n')
    return


def generate_adocs():
    for event_file in event_files:
        with open('event_files/' + event_file) as fr:
            data = json.load(fr)
            adoc_file = event_file.replace('.json', '.adoc')
            with open('gen/' + adoc_file, "w+") as fw:
                generate_event_adoc(data, fw, file_to_group[event_file])

    for metric_file in metric_files:
        with open('event_files/' + metric_file) as fr:
            data = json.load(fr)
            adoc_file = metric_file.replace('.json', '.adoc')
            with open('gen/' + adoc_file, "w+") as fw:
                generate_metric_adoc(data, fw, file_to_group[metric_file])
    return


if __name__ == '__main__':
    generate_adocs()
