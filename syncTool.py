import subprocess
import sys
import pyinotify


class MyEventHandler(pyinotify.ProcessEvent):
    def my_init(self, cwd):
        self.extensions = 'txt,py,php'.split(',')
        self.cwd = cwd

    def run_cmd(self, event):
        print 'modificando archivo %s' % event.pathname
        user = 'user'
        host = '192.168.1.1'
        cmd = 'scp %s %s@%s:%s' % (event.pathname, user, host, event.pathname)
        resp = subprocess.call(cmd, shell=True)
        print cmd        

    def process_IN_MODIFY(self, event):
        if all(not event.pathname.endswith(ext) for ext in self.extensions):
            return
        self.run_cmd(event)

    def process_IN_CREATE(self, event):
        if all(not event.pathname.endswith(ext) for ext in self.extensions):
            return
        self.run_cmd(event)

    def process_IN_DELETE(self, event):
        if all(not event.pathname.endswith(ext) for ext in self.extensions):
            return
        self.run_cmd(event)

def synchronize(path):
    wm = pyinotify.WatchManager()
    handler = MyEventHandler(cwd=path)
    notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
    wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
    print '==> Start monitoring %s (type c^c to exit)' % path
    notifier.loop()


if __name__ == '__main__':
    path = sys.argv[1]
    synchronize(path)
