from fabric.api import cd, run, sudo, put
from fabric.api import task, local


@task
def deploy():
    run('mkdir -p /home/davidchen/porkguy')
    put('./kube', '/home/davidchen/porkguy')
    with cd('/home/davidchen/porkguy/kube'):
        run('bash deploy.sh')
