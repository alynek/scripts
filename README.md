Commands to run:

chmod +x script_pipeline_template.sh
python3 script_pipeline_template.sh 'branch' 'workspace' 'repo'


commands tests:

python3 script_pipeline_template.sh 'main' '../workspace' 'https://github.com/alynek/ascii_art'

start jenkins:
    sudo service jenkins start