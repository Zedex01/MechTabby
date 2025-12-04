Matthew Moran 2025 05 26

This is my automated repo backup system.

All of my work projects are stored in local repos found at C:\Users\mmoran\Projects
however, git does not work well with syncing drives so I cannot use a remote repo. 
Instead, I automatically create bundles of the project repos which can be safely stored on the cloud.

BackupAll.bat is called once a task by task scheduler, it scans all the folders listed in ProjectList.txt
and checks if any of them have been updated by comparing hashes. if there is no change it will skip the project.