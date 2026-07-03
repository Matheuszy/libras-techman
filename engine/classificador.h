#ifndef CLASSIFICADOR_H
#define CLASSIFICADOR_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    float x;
    float y;
    float z;
} Landmark;

/*
=====================================================
FEATURE ENGINE (NÃO CLASSIFICA LETRAS)
=====================================================
*/

// calcula distância entre dois pontos
float calcular_distancia(Landmark p1, Landmark p2);

// detecta se dedo está estendido (helper)
int dedo_estendido(Landmark ponta, Landmark base);

// calcula abertura geral da mão
float calcular_abertura_mao(Landmark* hand_landmarks);

// export principal para Python
__declspec(dllexport)
void extrair_features(Landmark* hand_landmarks, float* output);

#ifdef __cplusplus
}
#endif

#endif