import multiprocessing
import subprocess

# extn_lst = [ 'control', 'adblock', 'ublock', 'privacy-badger',
#        "decentraleyes",
#        "disconnect",
#        "ghostery",
#        "https",
#        "noscript",
#        "scriptsafe",
#        "canvas-antifp",
#        "adguard"]
extn_lst = ['user-agent']

def get_domain(browser, extension):
    try:
        cmd = ["docker", "run", "--rm",
                "-v", "/dev/shm:/dev/shm",
                "-v", "./data:/data",
               "--security-opt", "seccomp=../seccomp.json",
               f"mpstat-{browser}",
               "--extensions", extension]
        # we can use "--shm-size=2g" instead of /dev/shm:/dev/shm
        
        run = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error in container for '{domain}': {e.output}")
    
    stdout = run.stdout.decode('utf-8')
    stderr = run.stderr.decode('utf-8')
    print('STDOUT:', stdout) 
    print('STDERR:', stderr)

for extn in extn_lst:
    get_domain('chrome', extn)

