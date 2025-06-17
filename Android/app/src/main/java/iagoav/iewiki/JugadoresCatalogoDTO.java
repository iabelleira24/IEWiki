package iagoav.iewiki;

public class JugadoresCatalogoDTO {
    private int id;
    private String name;
    private String image;

    public JugadoresCatalogoDTO(int id, String name, String image ) {
        this.id = id;
        this.name = name;
        this.image = image;


    }

    public int getId() {
        return id;
    }

    public String getNameJ() {
        return name;
    }

    public String getImageJ() {
        return image;
    }


}
