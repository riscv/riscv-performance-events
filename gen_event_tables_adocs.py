from pathlib import Path
import json
import os

event_files = []
metric_files = []

for file in os.listdir("event_files"):
    if file.endswith("_metrics.json"):
        metric_files.append(file)
    elif file.endswith(".json"):
        event_files.append(file)

def generate_event_adoc(data, out_file):
    #out_file.write('.' + group_name + ' group events\n')
    # out_file.write('[%unbreakable]\n')
    out_file.write('[width="100%",cols="35%,65%",options="header",]\n')
    out_file.write('|===\n')
    out_file.write('|Name |Description\n')
    for event in data:
        name = event['EventName']
        desc = event['PublicDescription']
        out_file.write('|' + name + ' |' + desc + '\n')
    out_file.write('|===\n\n')
    # out_file.write('[%unbreakable]\n')
    return


def generate_metric_adoc(data, out_file):
    #out_file.write('.' + group_name + ' group metrics\n')
    # out_file.write('[%unbreakable]\n')
    out_file.write('[width="100%",cols="25%,40%,35%",options="header",]\n')
    out_file.write('|===\n')
    out_file.write('|Name |Description |Formula\n')
    for metric in data:
        name = metric['MetricName']
        desc = metric['PublicDescription'] if 'PublicDescription' in metric else metric['BriefDescription']
        formula = metric['MetricExpr']
        out_file.write('|' + name + ' |' + desc + ' |' + formula + '\n')
    out_file.write('|===\n\n')
    # out_file.write('[%unbreakable]\n')
    return


def generate_adocs():
    for event_file in event_files:
        with open('event_files/' + event_file) as fr:
            data = json.load(fr)
            adoc_file = event_file.replace('.json', '.adoc')
            with open('adoc_event_tables/' + adoc_file, "w+") as fw:
                generate_event_adoc(data, fw)

    for metric_file in metric_files:
        with open('event_files/' + metric_file) as fr:
            data = json.load(fr)
            adoc_file = metric_file.replace('.json', '.adoc')
            with open('adoc_event_tables/' + adoc_file, "w+") as fw:
                generate_metric_adoc(data, fw)
    return


if __name__ == '__main__':
    generate_adocs()
