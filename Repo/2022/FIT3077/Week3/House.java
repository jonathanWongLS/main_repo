import java.util.*;

class House{
    private List<Person> listResidents;
    public House(List<Person> residents){
        this.listResidents =  residents;
    }
    public void addResident(Person resident){
        this.listResidents.add(resident);
    }
 }