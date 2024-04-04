from LightFMClass import LightFMRecSyc, moveis_fin, movies_to_predict, RecSycFilms, ClassRecSyc


lfm = LightFMRecSyc(model=ClassRecSyc,
                        RecSycFilms=RecSycFilms,
                        IMDb_df=moveis_fin,
                        Genre=None)

res = lfm.recommend(user_id=[1010], k=1, movies_to_predict=movies_to_predict)

print(res)