pipeline{
    agent any
    stages{
        stage('version'){
            steps{
                bat 'python --version'
            }
        }

        stage('attendance_MARK_IN'){
            steps{
                bat 'attendance_MARK_IN.py'
            }
        }
    }
}