﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectSetActive : MonoBehaviour
{

    public GameObject trigger2; 
    public GameObject highlight;

    private void Start()
    {
        trigger2.SetActive(false);
        highlight.SetActive(false);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Reverse_Gear"))
        {
            trigger2.SetActive(true); 
        }      
    }
}
