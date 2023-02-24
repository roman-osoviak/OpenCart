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
      stage('WorkWithYAMLfile'){
        steps {
          sh """
          sed -i 's~site_url_address_template~https://demo.opencart.com/index.php~g' config.yml
          """
          echo 'Trying to get site_url value'
          echo valuesYaml.environment.site_url
          echo 'URL received successfully'
        }
      }
    }
}