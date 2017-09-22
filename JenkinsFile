node {
   def mvnHome
   stage('test') { // for display purposes
      // Get some code from a GitHub repository
      git 'https://github.com/CodeN1nja/jenkins.git'
      def out = sh script: 'ls', returnStdout: true
      sh 'ls'
      sh 'sudo docker build -t zishanzee/poc .'
   }
}
