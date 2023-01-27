package com.deloitte.{{cookiecutter.project_name}};

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table
public class {{cookiecutter.resource_name}} {

    @Id
    private Long id;
}
