#!/usr/bin/env python3
if __name__ == "__main__":
        import difflib
        import os
        import datetime
        change = None
        if not os.path.exists('/old.txt'):
                os.mknod('/old.txt')
        if not os.path.exists('/diff.txt'):
                os.mknod('/diff.txt')
        with open('/old.txt') as old:
                old_text = old.readlines()
        with open('/new.txt') as new:
                new_text = new.readlines()
        with open("diff.txt", "w") as diff:
                date=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                diff.write(date+' Scan results:\n')
                for line in difflib.unified_diff(
                        old_text, new_text, fromfile='old.txt',
                        tofile='new.txt', lineterm=''):
                        if line.startswith('+') or line.startswith('-'):
                                diff.write(line+'\n')
                                change = True
                if change!=True:
                        diff.write("No additional or lost hosts since last scan.")
os.remove('/old.txt')
os.rename('/new.txt', '/old.txt')
