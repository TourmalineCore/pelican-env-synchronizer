import subprocess

subprocess.run("git clone https://github.com/TourmalineCore/pelican-local-env.git", shell=True, check=True)

subprocess.run("helmfile cache cleanup && helmfile --environment local --namespace local -f pelican-local-env/deploy/helmfile.yaml apply", shell=True, check=True)