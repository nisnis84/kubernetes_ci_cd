pipeline {
  agent none
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t my_docker_jenkins .'
      }
    }
  }
}