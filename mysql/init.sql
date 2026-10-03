CREATE DATABASE IF NOT EXISTS taskdb;

USE taskdb;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (title) VALUES
('Learn Docker'),
('Build a multi-container project'),
('Deploy application on AWS');
