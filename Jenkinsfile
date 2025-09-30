pipeline{
    agent any
    stages{
        stage('version'){
            steps{
                sh 'python3 --version'
            }
        }

        stage('attendance_MARK_IN'){
            steps{
                sh 'attendance_MARK_IN.py'
            }
        }
    }
}