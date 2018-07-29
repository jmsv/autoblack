#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time
from copy import deepcopy

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

__version__ = "0.1.a0"


class BlackEvent(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def process(self, event):
        """
        Run black command
        :param event: Watchdog file change event
        :return: Exit code: good-0, bad-1
        """
        if not os.path.exists(event.src_path):
            return 1

        print("File changed:", event.src_path)

        # Construct black command
        command = categorise_args()["options"]
        command.insert(0, "black")
        command.append(event.src_path)

        status = subprocess.call(command)
        print()
        return status

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


def categorise_args(args=deepcopy(sys.argv)):
    result = {"all": args, "paths": [], "options": []}

    for arg in args[1:]:
        if os.path.exists(arg):
            result["paths"].append(arg)
        else:
            result["options"].append(arg)

    return result


def main():
    autoblack_args = categorise_args()

    observer = Observer()

    black_event = BlackEvent()

    if len(autoblack_args["paths"]) < 1:
        # If no paths specified, watch current directory
        observer.schedule(black_event, ".", recursive=True)
    else:
        # Added observers for specified paths
        for path in autoblack_args["paths"]:
            if os.path.isfile(path):
                # TODO: Add support for individual files
                raise NotImplementedError("Can't watch files yet!")
            observer.schedule(black_event, path, recursive=True)

    observer.start()

    try:  # Run until interrupted (e.g. Ctrl-C)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    print()
