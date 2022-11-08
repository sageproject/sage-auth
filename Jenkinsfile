pipeline {
  agent any
  environment {
    IMAGE_NAME = "obliviobvious/sage-auth"
    dhcreds = 'DockerHubLogin'
    img = ''
  }
  stages {
    stage('Build') {
      steps {
        script {
          img = docker.build IMAGE_NAME
        }
      }
    }
    stage('Test') {
      steps {
        sh 'echo Running some tests...'
      }
    }
    stage('Publish') {
      steps {
        script {
          docker.withRegistry('', dhcreds) {
            img.push("0.0.${env.BUILD_ID}")
            img.push("latest")
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'kubectl get all'
      }
    }
  }
}