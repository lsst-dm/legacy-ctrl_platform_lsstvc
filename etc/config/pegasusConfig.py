config.platform.nodeSetRequired = True
config.platform.localScratch = "/scratch/$USER_NAME/condor_scratch"
config.platform.defaultRoot = "/scratch/$USER_NAME/condor_work"
config.platform.dataDirectory = "/datasets"
config.platform.fileSystemDomain = "ncsa.illinois.edu"
config.platform.scheduler = "slurm"
config.platform.manager = "pegasus"
config.platform.setup_using = "getenv"
