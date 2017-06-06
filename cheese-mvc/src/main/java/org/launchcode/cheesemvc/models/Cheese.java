package org.launchcode.cheesemvc.models;

/**
 * Created by lisette on 31/5/17.
 */
public class Cheese {

    private String cheeseName;
    private String cheeseDescription;

    public Cheese(String name, String description){
        this.cheeseName = name;
        this.cheeseDescription = description;
    }

    public String getCheeseName() {
        return cheeseName;
    }

    public void setCheeseName(String aCheeseName) {
        cheeseName = aCheeseName;
    }

    public String getCheeseDescription() {
        return cheeseDescription;
    }

    public void setCheeseDescription(String aCheeseDescription) {
        cheeseDescription = aCheeseDescription;
    }
}
