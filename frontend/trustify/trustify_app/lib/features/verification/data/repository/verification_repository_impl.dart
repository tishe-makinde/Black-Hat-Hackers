import 'package:dartz/dartz.dart';
import 'package:trustify_app/core/error/exceptions.dart';
import 'package:trustify_app/core/error/failure.dart';
import 'package:trustify_app/features/verification/data/data_sources/remote/verification_remote_data_source.dart';
import 'package:trustify_app/features/verification/domain/repository/verification_repository.dart';

class VerificationRepositoryImpl implements VerificationRepository {
  final VerificationRemoteDataSource _verificationRemoteDataSource;
  VerificationRepositoryImpl(this._verificationRemoteDataSource);
  @override
  Future<Either<Failure, Map<String, dynamic>>> verifyImage() {
    // TODO: implement verifyImage
    throw UnimplementedError();
  }

  @override
  Future<Either<Failure, Map<String, dynamic>>> verifyLink(String url) async {
    try {
      Map<String, dynamic> response =
          await _verificationRemoteDataSource.verifyLink(url);
      return right(response);
    } on VerificationException catch (e) {
      return left(Failure(e.toString()));
    }
  }
}
