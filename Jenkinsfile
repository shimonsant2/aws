pipeline {
    agent any
    stages {
        stage('Installing packages') {
            steps {
                script {
                    sh 'pwd'
                    sh 'ls -l'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Static Code Checking') {
            steps {
                script {
                    sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                    recordIssues(
                        tool: pyLint(pattern: 'pylint.log'),
                        unstableTotalHigh: 100,
                    )
                }
            }
        }
        stage ('for the fix branch') {
          when {
            branch "fix-*"
          }
          steps {
             echo 'this only run for the fixes'
            sh 'pwd'
           }
        }
        stage ('for the PR branch') {
          when {
            branch "PR-*"
          }
          steps {
             echo 'this only run for the PRs'
             sh 'pwd'
           }
        }
        stage('Running Unit tests') {
            steps {
                script {
                    sh 'python3 -m pytest --junitxml=pyunit.xml --cov=. --cov-report xml'
                    step([$class: 'CoberturaPublisher',
                        coberturaReportFile: "coverage.xml",
                        onlyStable: false,
                        failNoReports: true,
                        failUnhealthy: false,
                        failUnstable: false,
                        autoUpdateHealth: true,
                        autoUpdateStability: true,
                        zoomCoverageChart: true,
                        maxNumberOfBuilds: 10,
                        lineCoverageTargets: '9, 9, 9',
                        conditionalCoverageTargets: '10, 10, 10',
                        classCoverageTargets: '10, 10, 10',
                        fileCoverageTargets: '10, 10, 10',
                    ])
                    junit "pyunit.xml"
                }
            }
        }
    }
}