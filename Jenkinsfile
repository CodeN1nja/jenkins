node {
   def mvnHome
   stage('test') { // for display purposes
      // Get some code from a GitHub repository
      git 'https://github.com/CodeN1nja/jenkins.git'
      def out = sh script: 'ls', returnStdout: true
      sh 'ls'
      sh 'sudo docker build -t zishanzee/poc .'
      sh 'sudo docker push zishanzee/poc:latest'
      sh 'aws ecs register-task-definition file://task_definition.json --cli-input-json --region us-east-1'
      sh 'aws ecs update-service --service sample-webapp --task-definition console-sample-app-static:3 --region us-east-1'
   }
}
