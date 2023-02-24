def loadValuesYaml(){
  def valuesYaml = readYaml (file: 'config.yml')
  return valuesYaml;
}

pipeline {
    agent any

    stages {
      stage('CI/CD Initialization'){
        steps {
          script{
            valuesYaml = loadValuesYaml()
            println valuesYaml.getClass()
          }
        }
      }
      stage('WorkWithYAMLfile'){
        steps {
          sh """
          sed -i 's~site_url_address_template~https://demo.opencart.com/index.php~g' config.yml
          """
          echo 'Trying to get site_url value'
          echo valuesYaml.site_url
          echo 'URL received successfully'
        }
      }
    }
}