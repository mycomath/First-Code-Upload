/** A class to represent a Treasure in an adventure game.
 *  @see http://www.radford.edu/~itec120/2010fall-ibarland/Homeworks/hw04.html
 *  @author ibarland@radford.edu
 *  @version 2019-Oct-25
 */
class Treasure extends Object120 {

    /** The name of this treasure. */
    String name;
    /** A longer, textual description of this treasure. */
    String description;
    /** The weight of this Treasure, in lbs. */
    double weight;
    /** The URL of an image (jpg or gif or other standard type) showing this Treasure. */
    String imageURL;

    /** A URL used internally, if no better URL is provided for a Treasure.
     */
    static final String UNKNOWN_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/4/44/Question_mark_%28black_on_white%29.png";
    

    /** Treasure constructor.
     * @param n The name of this treasure.
     * @param d A longer, textual description of this treasure.
     * @param w The weight of this Treasure, in lbs.
     * @param _imageURL The URL of an image (jpg or gif or other standard type) showing this Treasure,
     *                  or the empty String.
     */
    Treasure( String n, String d, double w, String u ) {
        this.name = n;
        this.description = d;
        this.weight = w;
        this.imageURL = u.equals("") ? UNKNOWN_IMAGE_URL : u;
    }

    String getName () {
        return this.name;
    }
    
    void setName (String n) {
        this.name = n;
    }
    
    String getDescription () {
        return this.description;
    }
    
    void setDescription (String n) {
        this.description = n;
    }
    
    double getWeight () {
        return this.weight;
    }
    
    void setWeight (double r) {
        this.weight = r;
    }
    
    String getImageURL () {
        return this.imageURL;
    }
    
    void setImageURL (String url) {
        this.imageURL = url;
    }
    
    /** Change the description and image url of a treasure.
     * @param d The new desired description.
     * @param url The new desired image url.
     */
    void polymorph (String d, String url) {
        this.setDescription(d);
        String a = url.equals("") ? UNKNOWN_IMAGE_URL : url;
        this.setImageURL(a);
    }
        
    /** Return a short, user-friendly description the given Treasure.
     * @param t The treasure to describe.
     * @return a short, user-friendly description of t.
     */
    String toPrettyString() {
        String pluralize = (this.getWeight() != 1.0) ? "s" : "";
        return this.getName() + " (" + this.getWeight() + " lb" + pluralize + ")";
    }

    /** Return a new piece of lint. */
    static Treasure newLint() {
        return new Treasure("lint", "a bit of fuzz", 0.0, "");
        }
    
    
    /** Is a treasure merely lint?
     * @return true if (and only if) `t` is lint.
     */
    boolean isLint() {
        return (this.getWeight() == 0.0) && "lint".equals(this.getName().toLowerCase());
    }

    /** Is one treasure better than another?
     * @return true if (and only if) thiss is considered better than thatt
     *  Currently it just means it weighs more than the other Treasure, although
     *  that criterion is subject to future change.
     */
    boolean isBetterThan(Treasure thatt) {
        return (this.getWeight() < thatt.getWeight())
            && !this.isLint();
    }

    /** Return a counterfeit copy of a Treasure.
     * @param t the Treasure to counterfeit.
     * @return a counterfeit copy of t.
     */
    Treasure counterfeit() {
        int desrcLen = this.getDescription().length();
        String updatedDescr = this.getDescription().substring(0, desrcLen-1)
                            + ", but it feels a bit chintzy"
                            + this.getDescription().substring(desrcLen-1, desrcLen);
        return new Treasure(this.getName(), updatedDescr, this.getWeight()/2.0, this.getImageURL());
    }

  
    /**************************************************************************/
    /** Test our functions:
     * Create several instances of Treasures,
     * and call methods on them.
     */
    static void testTreasure() {
        Treasure t1 = new Treasure( "a hot potato",
                "Upwards of 400F (204C).",
                1.0,
                "" );
        Treasure t2 = new Treasure( "a blue whale",
                "It's actually pink, but he's very very sad.",
                20000.0,
                "http://www.argyleacademy.com/uploaded_images/whale-764874.jpg" );
        Treasure t3 = new Treasure( "a Captain Janeway action figure",
                "OMG, NIB!",
                2.2,
                "http://farm2.static.flickr.com/1362/851258803_32ab150fe9_o.jpg" );
        Treasure trueLint = new Treasure("lint", "Fuzzy.", 0.0, "");
        Treasure fauxLint = new Treasure("lint", "Fuzzy.", 7.1, "");

        printTestMsg("toPrettyString");
        assertEquals( (t1).toPrettyString(), "a hot potato (1.0 lb)" );
        assertEquals( (t3).toPrettyString(), "a Captain Janeway action figure (2.2 lbs)" );
        
        printTestMsg("polymorph");
        
        Treasure testLint = newLint();
        assertEquals( testLint.getName(), "lint");
        assertEquals( testLint.getDescription(), "a bit of fuzz");
        assertEquals( testLint.getImageURL(), UNKNOWN_IMAGE_URL);
        testLint.polymorph("Zombie Lint", "bloody note");
        assertEquals( testLint.getName(), "lint");
        assertEquals( testLint.getDescription(), "Zombie Lint");
        assertEquals( testLint.getImageURL(), "bloody note");
        
        Treasure dog = new Treasure ("Benny", "Statue of a dog", 12.3, "benny.jpg");
        assertEquals( dog.getName(), "Benny");
        assertEquals( dog.getDescription(), "Statue of a dog");
        assertEquals( dog.getImageURL(), "benny.jpg");
        dog.polymorph("Sheep statue", "");
        assertEquals( dog.getName(), "Benny");
        assertEquals( dog.getDescription(), "Sheep statue");
        assertEquals( dog.getImageURL(), UNKNOWN_IMAGE_URL);
        
        Treasure myLint = newLint();
        assertEquals( myLint.getName(), "lint" );
        assertEquals( myLint.getWeight(), 0.0 );
        
        printTestMsg("isLint");
        assertEquals( t1.isLint(), false );
        assertEquals( trueLint.isLint(), true );
        assertEquals( fauxLint.isLint(), false );

        printTestMsg("isBetterThan");
        assertEquals( t1.isBetterThan(t2), true );
        assertEquals( t2.isBetterThan(t1), false );
        assertEquals( t1.isBetterThan(t1), false );

        printTestMsg("counterfeit");
        assertEquals( t2.counterfeit(),
                      new Treasure( "a blue whale",
                                    "It's actually pink, but he's very very sad, but it feels a bit chintzy.",
                                    10000.0,
                                    t2.getImageURL() ) );
         
        assertEquals( trueLint.counterfeit(),
                      new Treasure( "lint",
                                    "Fuzzy, but it feels a bit chintzy.",
                                    0.0,
                                    "" ) );

        printTestSummary();
    }

    public static void main( String[] args ) {
        testTreasure();
        };

}
