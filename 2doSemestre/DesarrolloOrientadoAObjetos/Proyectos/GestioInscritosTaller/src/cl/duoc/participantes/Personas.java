package cl.duoc.participantes;

public class Personas {
    public class Participante {

        // -------------------------------
        // Atributos privados
        // -------------------------------
        private String rut;
        private String nombre;
        private String email;
        private boolean activo; // true = inscrito, false = inactivo

        // -------------------------------
        // Constructor completo
        // -------------------------------
        public Participante(String rut, String nombre, String email, boolean activo) {
            this.rut = rut;
            this.nombre = nombre;
            this.email = email;
            this.activo = activo;
        }

        // -------------------------------
        // Getters y Setters
        // -------------------------------
        public String getRut() {
            return rut;
        }

        public void setRut(String rut) {
            this.rut = rut;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public boolean isActivo() {
            return activo;
        }

        public void setActivo(boolean activo) {
            this.activo = activo;
        }

        // -------------------------------
        // Método toString
        // -------------------------------
        @Override
        public String toString() {
            String estado = activo ? "Activo" : "Inactivo";
            return "Participante{" +
                    "RUT='" + rut + '\'' +
                    ", Nombre='" + nombre + '\'' +
                    ", Email='" + email + '\'' +
                    ", Estado=" + estado +
                    '}';
        }

        // -------------------------------
        // (Opcional) equals y hashCode basados en RUT
        // -------------------------------
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Participante that = (Participante) obj;
            return rut.equals(that.rut);
        }

        @Override
        public int hashCode() {
            return rut.hashCode();
        }
    }
}
