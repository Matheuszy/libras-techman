#include "classificador.h"
#include <math.h>

float calcular_distancia(Landmark p1, Landmark p2) {
    return sqrtf(
        powf(p1.x - p2.x, 2) +
        powf(p1.y - p2.y, 2) +
        powf(p1.z - p2.z, 2)
    );
}

int dedo_estendido(Landmark ponta, Landmark base) {
    return ponta.y < base.y;
}

float calcular_abertura_mao(Landmark* lm) {
    return calcular_distancia(lm[8], lm[0]);
}

__declspec(dllexport)
void extrair_features(Landmark* lm, float* output)
{
    output[0] = calcular_distancia(lm[4], lm[8]);
    output[1] = calcular_distancia(lm[8], lm[12]);
    output[2] = calcular_distancia(lm[12], lm[16]);
    output[3] = calcular_distancia(lm[16], lm[20]);

    output[4] = calcular_abertura_mao(lm);

    output[5] = dedo_estendido(lm[8], lm[6]);
    output[6] = dedo_estendido(lm[12], lm[10]);
    output[7] = dedo_estendido(lm[16], lm[14]);
    output[8] = dedo_estendido(lm[20], lm[18]);
}