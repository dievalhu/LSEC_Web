GRANT ALL PRIVILEGES ON ecuadorian_Sign_Language_base.* TO 'ecuadorian_Sign_Language_user'@'%' IDENTIFIED BY 'tesisroot';
FLUSH PRIVILEGES;


-- Asigna todos los privilegios a 'ecuadorian_Sign_Language_user' en la base de datos 'ecuadorian_Sign_Language_base' desde cualquier dirección (%).
-- Otorga todos los permisos globales con algunas restricciones

GRANT ALL PRIVILEGES ON *.* TO 'ecuadorian_Sign_Language_user'@'%' 
  REQUIRE NONE 
  WITH GRANT OPTION 
  MAX_QUERIES_PER_HOUR 0 
  MAX_CONNECTIONS_PER_HOUR 0 
  MAX_UPDATES_PER_HOUR 0 
  MAX_USER_CONNECTIONS 0;

-- Otorga permisos SELECT específicos para una base de datos
GRANT SELECT ON specific_database.* TO 'ecuadorian_Sign_Language_user'@'%';

-- Otorga permisos para una base de datos específica
GRANT INSERT, UPDATE, DELETE ON another_database.* TO 'ecuadorian_Sign_Language_user'@'%';

FLUSH PRIVILEGES;



