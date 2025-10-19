import 'package:get_it/get_it.dart';
import 'package:trustify_app/features/verification/data/data_sources/remote/verification_remote_data_source.dart';
import 'package:trustify_app/features/verification/data/repository/verification_repository_impl.dart';
import 'package:trustify_app/features/verification/domain/repository/verification_repository.dart';
import 'package:trustify_app/features/verification/domain/usecases/verify_link_use_case.dart';
import 'package:trustify_app/features/verification/presentation/bloc/verification_bloc.dart';

final GetIt serviceLocator = GetIt.instance;

void initDependencies() {
  _initVerification();
}

void _initVerification() {
  serviceLocator.registerFactory<VerificationRemoteDataSource>(
      () => VerificationRemoteDataSourceImpl());

  serviceLocator.registerFactory<VerificationRepository>(
      () => VerificationRepositoryImpl(serviceLocator()));

  serviceLocator.registerFactory<VerifyLinkUseCase>(
      () => VerifyLinkUseCase(serviceLocator()));

  serviceLocator.registerLazySingleton<VerificationBloc>(
    () => VerificationBloc(
      serviceLocator(),
    ),
  );
}
