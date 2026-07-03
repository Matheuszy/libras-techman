#include <stdio.h>
#include <math.h>

typedef struct {
    float x;
    float y;
    float z;
} Landmark;

float calcular_distancia(Landmark p1, Landmark p2) {
    return sqrtf(powf(p1.x - p2.x, 2) + powf(p1.y - p2.y, 2) + powf(p1.z - p2.z, 2));
}

__declspec(dllexport) char classificar_libras(Landmark* hand_landmarks) {int ind_estendido = (hand_landmarks[8].y < hand_landmarks[6].y);
    int med_estendido = (hand_landmarks[12].y < hand_landmarks[10].y);
    int ane_estendido = (hand_landmarks[16].y < hand_landmarks[14].y);
    int min_estendido = (hand_landmarks[20].y < hand_landmarks[18].y);
    
    if (!ind_estendido && !med_estendido && !ane_estendido && !min_estendido) {
        if (hand_landmarks[4].x > hand_landmarks[5].x) {
            return 'A';
        }
        return 'O';
    }

        if (hand_landmarks[4].x < hand_landmarks[2].x || hand_landmarks[4].x > hand_landmarks[17].x) {
            return 'L';
        }
    }
    

    }
    

    }
    

    }
        }
    }
    
    }

    return '?';
}