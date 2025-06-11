package iagoav.iewiki;

public class JugadoresDTO {
    private int id;
    private String name;
    private String position;
    private String image;



    public JugadoresDTO(int id, String name, String position,  String image ) {
        this.id = id;
        this.name = name;
        this.position = position;
        this.image = image;


    }

    public int getId() {
        return id;
    }

    public String getNameJ() {
        return name;
    }
    public String getPositionJ() {
        return position;
    }

    public String getImageJ() {
        return image;
    }

}
