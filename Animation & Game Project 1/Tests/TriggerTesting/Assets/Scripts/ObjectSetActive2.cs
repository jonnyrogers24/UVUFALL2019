using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectSetActive2 : MonoBehaviour
{

    public GameObject highlight;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Reverse_Gear"))
        {
            highlight.SetActive(true); 
        }      
    }
}
