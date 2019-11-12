using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;
public class MenuManager : MonoBehaviour
{
    public GameObject mainMenu;
    public GameObject subMenu;
    // Start is called before the first frame update
    void Start()
    {
        mainMenu.SetActive(true);
        subMenu.SetActive(false);
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void Menu()
    {
        mainMenu.SetActive(false);
        subMenu.SetActive(true);
    }

    public void QuitMenu()
    {
        SceneManager.LoadScene("Start_Menu_test"); 
    }

    public void Back()
    {
        mainMenu.SetActive(true);
        subMenu.SetActive(false);
    }
}
