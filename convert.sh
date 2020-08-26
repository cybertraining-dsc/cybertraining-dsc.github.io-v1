cp -r  ./book/chapters/devops/images ./content/en/modules/devops

bookmanager-markdown.py "book/chapters/devops/devop-ci.md" --weight 2 --description "Indorduction to DevOps and Continious Integration"
bookmanager-markdown.py "book/chapters/devops/devops-iac.md" --weight 5 --description "Infrastructure as Code is the ability of code to generate, maintain and destroy application infrastructure like server, storage and networking, without requiring manual changes."

bookmanager-markdown.py "book/chapters/devops/ansible.md" --weight 10 --description "Ansible is an open-source IT automation DevOps engine allowing you to manage and configure many compute resources in a scalable, consistent and reliable way."

bookmanager-markdown.py "book/chapters/devops/puppet.md" --weight 20 --description "Puppet is configuration management tool that simplifies complex task of deploying new software, applying software updates and rollback software packages in large cluster "

bookmanager-markdown.py "book/chapters/devops/travis.md" --weight 30 --description "Travis CI is a continuous integration tool that is often used as part of DevOps development. It is a hosted service that enables users to test their projects on GitHub."

bookmanager-markdown.py "book/chapters/devops/devop-aws.md" --weight 40 --description "AWS cloud offering comes with end-to-end scalable and most performant support for DevOps"

bookmanager-markdown.py "book/chapters/devops/devop-azure-monitor.md" --weight 50 --description "Microsoft provides unified tool called Azure Monitor for end-to-end monitoring of the infrastructure and deployed applications."
