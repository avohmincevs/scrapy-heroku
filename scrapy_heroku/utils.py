import os
from spiderqueue import Psycopg2SpiderQueue


def get_project_list(config):
    """Get list of projects by inspecting the eggs dir
        scrapyd.conf is skipped. Only explicitly defined projects
    """
    
    eggs_dir = config.get('eggs_dir', 'eggs')
    if os.path.exists(eggs_dir):
        projects = os.listdir(eggs_dir)
    else:
        projects = []
    print projects
    return projects

def get_spider_queues(config):
    queues = {}
    for project in get_project_list(config):
        table = 'scrapy_%s_queue' % project
        queues[project] = Psycopg2SpiderQueue(config, table=table)
    return queues
