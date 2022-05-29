"use strict"
function series(n)
{
    let ar = [11,9,20,20,25];
    let divisibleByThree = 0;
    let nextTerm = 0;
    let index = ar.length-1;
    
    while (index < n)
    {
        nextTerm = ar[index]+ar[index-1]+ar[index-2]+ar[index-3]+ar[index-4];
        ar.push(nextTerm);
        index++;
    }

    for(let i = 0; i < ar.length; i++)
    {
        if(ar[i]%3 === 0)
        {
            divisibleByThree++;
        }
    }

    return divisibleByThree;
}

console.log(series(950594162316416));
