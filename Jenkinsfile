node {
   def mvnHome
   stage('docker push') { // for display purposes
      // Get some code from a GitHub repository
      git 'https://github.com/CodeN1nja/jenkins.git'
      def out = sh script: 'ls', returnStdout: true
      sh 'ls'
      sh 'sudo docker build -t zishanzee/poc .'
      sh 'sudo docker push zishanzee/poc:latest'
   }
   stage('generate task definition') {
      sh 'sudo aws ecs register-task-definition --cli-input-json file://task_definition.json --region us-east-1 > taskdef.json'
      sh 'taskdef=`cat taskdef.json`'
      sh 'echo $taskdef'
   }
   stage('update task definition') {
      sh 'echo $taskdef'
      sh 'python revision.py taskdef.json > rev'
      sh 'cat rev'
      sh 'sudo aws ecs update-service --service sample-webapp --task-definition console-sample-app-static:$(cat rev) --region us-east-1'
   }
}
