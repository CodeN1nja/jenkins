node {
   def mvnHome
   stage('test') { // for display purposes
      // Get some code from a GitHub repository
      git 'https://github.com/CodeN1nja/jenkins.git'
      def out = sh script: 'ls', returnStdout: true
      sh 'ls'
      sh 'sudo docker build -t zishanzee/poc .'
      sh 'sudo docker push zishanzee/poc:latest'
      sh 'sudo aws s3 ls'
      sh ('sudo aws ecs register-task-definition --cli-input-json file://task_definition.json --region us-east-1 > test.json')
      sh 'test = cat test.json'
   }
   stage('2') {
      sh 'cat test.json'
      sh 'rev="$(python revision.py test.json)"'
      sh 'echo $rev'
      sh 'sudo aws ecs update-service --service sample-webapp --task-definition console-sample-app-static:$rev --region us-east-1'
   }
}
