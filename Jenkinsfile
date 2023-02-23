def loadValuesYaml(){
  def valuesYaml = readYaml (file: 'config.yml')
  return valuesYaml;
}

pipeline {
    agent any

    stages {
      stage('First Stage'){
        steps {
          echo 'Hello Jenkins!!!'
          }
        }
      }
    }
}