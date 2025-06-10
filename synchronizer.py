import os

os.system("git clone https://github.com/TourmalineCore/pelican-local-env.git")

os.system("helmfile cache cleanup && helmfile --environment local --namespace local -f pelican-local-env/deploy/helmfile.yaml apply")