package org.launchcode.cheesemvc.Controllers;

import org.launchcode.cheesemvc.models.Cheese;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import java.util.HashMap;
import javax.servlet.http.HttpServlet;
import java.util.ArrayList;


/**
 * Created by lisette on 18/5/17.
 */
@Controller
@RequestMapping("cheese")
public class CheeseController {

    //static ArrayList<String> cheeses = new ArrayList<>();

    static ArrayList<Cheese> cheeses = new ArrayList<>();
    //the above between <> can be any objects. It is not a holder for data type.
    //Request path: /cheese
    @RequestMapping(value = "")
    public String index(Model model) {
        // this is responsible for passing data to be displayed on index page
        model.addAttribute("cheeses", cheeses);
        //above connects the controller to the template.
        model.addAttribute("title", "Les fromages");
        return "cheese/index";
    }

    @RequestMapping(value = "add", method = RequestMethod.GET)
    public String displayAddCheeseForm(Model model) {
        model.addAttribute("title", "Entrez un fromage");
        return "cheese/add";
    }

    @RequestMapping(value = "add", method = RequestMethod.POST)
    public String processAddCheeseForm(@RequestParam String cheeseName, @RequestParam String cheeseDescription) {
        // This should send data to the first method
//        Cheese newCheese = new Cheese();
//        // above is an new instance of a Cheese object.
//        newCheese.setCheeseName(cheeseName);
//        newCheese.setCheeseDescription(cheeseDescription);
        Cheese newCheese = new Cheese(cheeseName, cheeseDescription);
        cheeses.add(newCheese);
        //Redirect to /cheese
        return "redirect:";
    }
    @RequestMapping(value = "remove", method = RequestMethod.POST)
    public String  displayRemoveCheeseForm(Model model) {
        model.addAttribute("cheeses", cheeses);
        model.addAttribute("title", "Remove Cheese");
        return "cheese/remove";
    }
}
