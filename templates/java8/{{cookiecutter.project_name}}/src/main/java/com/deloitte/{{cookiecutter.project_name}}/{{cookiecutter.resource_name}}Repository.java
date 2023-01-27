package com.deloitte.{{cookiecutter.project_name}};

import org.springframework.data.jpa.repository.JpaRepository;

public interface {{cookiecutter.resource_name}}Repository extends JpaRepository<{{cookiecutter.resource_name}}, Long> {
}