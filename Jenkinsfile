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
        sh 'echo Building $TAG_NAME'
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
      //when { tag 'v*' }
      steps {
        script {
          docker.withRegistry('', dhcreds) {
            img.push("0.0.${env.BUILD_ID}")
            img.push("latest")
          }
        }
      }
    }
    stage('Deploy Staging') {
      when { tag 'dev*' }
      steps {
        cd 'deploy'
        sh 'kubectl apply -f .'
      }
    }
    stage('Deploy Prod') {
      //when { tag 'v*' }
      steps {
        sh 'cd deploy'
        sh 'kubectl apply -f .'
      }
    }
  }
}