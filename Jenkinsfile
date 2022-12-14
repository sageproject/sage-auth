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
        dir('deploy') {
          sh 'kubectl apply -f sage-auth.yaml'
        }
      }
    }
    stage('Deploy Prod') {
      //when { tag 'v*' }
      steps {
        dir('deploy') {
          sh 'kubectl apply -f sage-auth.yaml'
        }
      }
    }
  }
}