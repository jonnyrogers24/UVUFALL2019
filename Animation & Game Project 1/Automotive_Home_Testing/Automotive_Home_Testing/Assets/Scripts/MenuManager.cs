using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class MenuManager : MonoBehaviour
{
    public GameObject mainMenu;

    public GameObject resetTimerButton;
    // Start is called before the first frame update
    void Start()
    {
        mainMenu.SetActive(true);
        resetTimerButton.SetActive(false);
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void Menu()
    {
        mainMenu.SetActive(false);
        resetTimerButton.SetActive(true);
    }
    
    public void SubMenu()
    {
        
    }
}
