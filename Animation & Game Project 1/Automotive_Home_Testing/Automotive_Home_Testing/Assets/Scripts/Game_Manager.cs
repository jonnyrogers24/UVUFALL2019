using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Game_Manager : MonoBehaviour
{
    public GameObject enterSim; 
    // Start is called before the first frame update
    public void EnterSim()
    {
        SceneManager.LoadScene("Home_Testing");
    }
}
