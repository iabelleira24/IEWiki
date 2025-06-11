package iagoav.iewiki;

public class TeamDTO {
    private int id;
    private String name;
    private String coach;
    private String image;

    public TeamDTO(int id, String name, String coach, String image) {
        this.id = id;
        this.name = name;
        this.coach = coach;
        this.image = image;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getCoach() {
        return coach;
    }

    public String getImage() {
        return image;
    }

}
